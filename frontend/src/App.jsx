import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import './App.css'
import DashBoard from './components/DashBoard'
import { Results } from './components/Results'

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<DashBoard />}></Route>
        <Route path='/results' element={<Results />}></Route>
      </Routes>
    </>

  )
}

export default App
