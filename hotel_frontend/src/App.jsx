import { useState } from 'react'
import { Button } from 'antd'
import { default as axios } from 'axios'


function App() {

  const DEFAULT_URLS = 'http://localhost:8000/'

  const [text, setText] = useState("")

  const clickBtn = async (x) => {
    const response = await axios.get(DEFAULT_URLS+'hotel/'+x)
    console.log(response.data)
  }
  

  return (
    <>
    <h1>Hello World</h1>
    <Button onClick={() => clickBtn('customer')}>Get customer</Button>
    <Button onClick={() => clickBtn('room')}>Get room</Button>
    <Button onClick={() => clickBtn('booking')}>Get booking</Button>
    <h2>{text}</h2>
    </>
  )
}

export default App
