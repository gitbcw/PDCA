from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.database.database import insert_task, get_all_tasks, update_task_status, delete_task 
from llm import call_llm_with_prompt
from prompts_loader import load_prompt
from bson import ObjectId  # 添加此行以导入 ObjectId

router = APIRouter()

# 定义请求模型
class TaskGenerationRequest(BaseModel):
    user_input: str  # 用户输入的文本信息

# 定义任务数据模型
class Task(BaseModel):
    description: str
    status: str = 'pending'

# 生成任务的接口
@router.post("/generate_tasks", response_model=List[Task])
async def generate_tasks(request: TaskGenerationRequest):
    try:
        # 加载任务生成的 prompt
        prompt = load_prompt("task_generation.txt")

        # 使用封装的 LLM 模块生成任务
        llm_response = call_llm_with_prompt(prompt, request.user_input)

        # 解析 LLM 的响应结果为任务列表
        tasks_text = llm_response.strip().split("\n")
        tasks = [{"description": task.strip(), "status": "pending"} for task in tasks_text if task.strip()]

        # 将任务存储到数据库中
        task_ids = []
        for task in tasks:
            task_id = insert_task(task)
            task_ids.append(str(task_id))
        
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"任务生成失败: {str(e)}")


# 将 BSON ObjectId 转换为字符串，以便返回给客户端
def task_to_json(task):
    task["_id"] = str(task["_id"])
    return task

# 保存任务到 MongoDB
@router.post("/save_tasks")
async def save_tasks(new_tasks: List[Task]):
    try:
        task_ids = []
        for task in new_tasks:
            task_dict = task.dict()  # 将 Pydantic 模型转换为字典
            task_id = insert_task(task_dict)  # 插入任务
            task_ids.append(str(task_id))
        return {"message": "Tasks saved successfully", "task_ids": task_ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取所有任务
@router.get("/tasks", response_model=List[Task])
async def get_tasks():
    try:
        tasks = get_all_tasks()
        tasks = [task_to_json(task) for task in tasks]  # 转换任务的 ObjectId 为字符串
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 更新任务状态
@router.put("/tasks/{task_id}")
async def update_task(task_id: str, status: str):
    try:
        result = update_task_status(ObjectId(task_id), status)  # 确保 update_task_status 已导入
        if result == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 删除任务
@router.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    try:
        result = delete_task(ObjectId(task_id))
        if result == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
