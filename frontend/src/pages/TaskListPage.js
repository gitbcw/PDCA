import React, { useEffect, useState } from 'react';
import { fetchTasks } from '../services/api';


function TaskListPage() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetchTasks()
            .then(response => {
                setTasks(response.data);
            })
            .catch(error => {
                console.error('获取任务列表失败：', error);
            });
    }, []);

    return (
        <div>
            <h1>任务列表</h1>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        {task.task_content}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TaskListPage;
