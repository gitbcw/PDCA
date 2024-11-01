import Mock from 'mockjs';

Mock.mock('/api/tasks', 'get', {
    code: 200,
    data: [
        { id: 1, task_content: '任务一', status: '未完成' },
        { id: 2, task_content: '任务二', status: '进行中' },
    ],
});

Mock.mock('/api/input', 'post', {
    code: 200,
    message: '提交成功',
});
