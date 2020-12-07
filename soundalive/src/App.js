import logo from './logo.svg';
import {useState} from 'react';
import './App.css';
import File from './File.js';
import WebRecorder from './WavRecorder';
function App() {
  const [submittedFile, setSubmittedFile] = useState(false);
  const [animal, setAnimal]= useState(null);
  const [time, setTime] = useState(null);
  function handleSubmit(animal, time) {
    setSubmittedFile(true);
    setAnimal(animal);
    setTime(time);
  }
  return (
    <div className="App">
      <header className="App-header">
        {!submittedFile ?
        <div>
        <WebRecorder onFileSend={handleSubmit}/>
        <File onFileSend={handleSubmit}/>
        </div>
        :
        <div>
        <p> your animal is: {animal}</p>
        <p> Found in {time}</p>
        </div>
      }
        <img src={logo} className="App-logo" alt="logo" />
        <p>
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
