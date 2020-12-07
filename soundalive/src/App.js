import logo from './logo.svg';
import {useState} from 'react';
import './App.css';
import File from './File.js';
//import WebRecorder from './WavRecorder';


function App() {
  const [submittedFile, setSubmittedFile] = useState(false);
  const [animal, setAnimal]= useState(null);
  const [bTime, setBTime] = useState(null);
  const [sTime, setSTime] = useState(null);
  const [otherMatches, setOtherMatches] = useState(null);
  const [image, setImage]= useState(logo);
  function handleSubmit(animal, sTime, bTime, set) {
    setSubmittedFile(true);
    setAnimal(animal);
    setBTime(bTime);
    setSTime(sTime);
    setImage(logo);
    setOtherMatches(set);
    console.log(otherMatches);
    console.log(set);
    setOtherMatches(set);
    /*    var myHeaders = new Headers();
    myHeaders.append("x-rapidapi-key", "de103cb136msh54049396c04d9aap1b6bffjsnbab7cfaebe8f");
    myHeaders.append("x-rapidapi-host", "bing-image-search1.p.rapidapi.com");

    var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
    };

    fetch("https://bing-image-search1.p.rapidapi.com/images/search?q="+animal+"&count=1", requestOptions)
    .then(response => response.json())
    .then(result => setImage(result.value[0].thumbnailUrl))
    .catch(error => console.log('error', error));*/

  }
  return (
    <div className="App">
      <header className="App-header">
        <h2> Sound Alive</h2>
        <h3>What animal is it? </h3>
        {!submittedFile ?
        <div>
      {/*
        <WebRecorder onFileSend={handleSubmit}/>
      */}
        <File onFileSend={handleSubmit}/>
        </div>
        :
        <div>
        <p> your animal is: {animal}</p>
        <p> B-tree found in: {bTime}</p>
        <p> Splay tree found in: {sTime}</p>

        <img src={image} className="App-logo" alt="logo" />

        </div>
      }
        <p>
        </p>
        <a
          className="App-link"
          href="https://www.macaulaylibrary.org/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Our Data Source
        </a>
      </header>
    </div>
  );
}

export default App;
