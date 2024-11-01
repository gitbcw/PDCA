import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InputPage from './pages/InputPage';
import TaskListPage from './pages/TaskListPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InputPage />} />
        <Route path="/tasks" element={<TaskListPage />} />
      </Routes>
    </Router>
  );
}

export default App;
