import React, { useState } from 'react';
import { Input, Button, message } from 'antd';
import { submitInput } from '../services/api';

function InputPage() {
    const [inputValue, setInputValue] = useState('');

    const handleSubmit = () => {
        submitInput(inputValue)
            .then(response => {
                message.success('提交成功');
                window.location.href = '/tasks';
            })
            .catch(error => {
                message.error('提交失败');
            });
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>任务生成器</h1>
            <Input.TextArea
                value={inputValue}
                onChange={e => setInputValue(e.target.value)}
                placeholder="请输入内容"
                rows={10}
            />
            <Button type="primary" onClick={handleSubmit} style={{ marginTop: '10px' }}>
                提交
            </Button>
        </div>
    );
}

export default InputPage;
