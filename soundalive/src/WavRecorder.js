//NOT SUPPORTED DO NOT USE
import React, {useState} from 'react';
import {useReactMediaRecorder} from "react-media-recorder";

const Record = props => {

  const [submitted] = useState(false);
  const [animal]= useState('');
  const {
    status,
    startRecording,
    stopRecording,
    mediaBlobUrl,
  } = useReactMediaRecorder({ audio: true });
  let submit = async () => {
    console.log(mediaBlobUrl);
    let blob = await fetch(mediaBlobUrl).then(r => r.blob());
    console.log(blob);
    var reader = new FileReader();
    reader.readAsDataURL(blob);
    var base64String;
    reader.onloadend = await function () {
      base64String = reader.result;

      // Simply Print the Base64 Encoded String,
      // without additional data: Attributes.

      console.log(base64String);
      console.log(typeof base64String)
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify({"content":base64String});

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
          };

          fetch("https://apangasa.pythonanywhere.com/process-audio", requestOptions)
          .then(response => response.text())
          .then(result => console.log(result))
          .then(props.onFileSend("animal", "time"))
          .catch(error => console.log('error', error));
          console.log(animal);
        }
  }

  return (
    <div>
    {!submitted ?
      <>
      <p>{status}</p>
      <button onClick={startRecording}>Start Recording</button>
      <button onClick={stopRecording}>Stop Recording</button>
      <audio src={mediaBlobUrl} controls autoPlay loop />
      <button onClick={submit}> Submit </button> </>
      : <p> Submitted </p> }
    </div>
  );
}

class WebRecorder extends React.Component {
  constructor(props){
    super(props);
    this.state = {
    };
  }

  render(){
    return (
      <div className="Recorder">
        <Record onFileSend={this.props.onFileSend}/>
      </div>
    );
  }
}

export default WebRecorder;
