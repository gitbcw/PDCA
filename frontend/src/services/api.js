import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:5000'; // 后端服务器地址

export const submitInput = (content) => {
    return axios.post('/api/input', { content });
};

export const fetchTasks = () => {
    return axios.get('/api/tasks');
};
