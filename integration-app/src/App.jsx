import { useEffect, useState } from 'react'
import axios from "axios"
function App() {
  
  
  
  
  const [msg, setMsg] = useState("")
  
  const make_api_call = async ()=>{
    const {data} = await axios.get(`http://localhost:8000/`)
    const {msg} = data;
    setMsg(msg)
  }
  
  useEffect(()=>{
    make_api_call()
  },[]); 
  
  return (
    <>
      <h1>{msg}</h1>
    </>
  )
}

export default App
