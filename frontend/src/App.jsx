import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'
import DashBoard from './components/DashBoard'
import { Results } from './components/Results'
import { History } from './components/History'
import { NotFound } from './components/NotFound'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<DashBoard />}></Route>
        <Route path='/results' element={<Results />}></Route>
        <Route path="/history" element={<History />}></Route>
        <Route path="*" element={<NotFound/>} />
      </Routes>
    </>

  )
}

export default App
