//NOT SUPPORTED DO NOT USE
import React from 'react';
import MicRecorder from 'mic-recorder-to-mp3';
import WebAudioRecorder from 'web-audio-recorder-js'
import { ReactMic } from 'react-mic';
const Mp3Recorder = new MicRecorder({ bitRate: 128 });
const recorder = new WebAudioRecorder();
class WebRecorder extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      isRecording: false,
      blobURL: '',
      isBlocked: false,
      record: false
    };
  }

  start = () => {
    if (this.state.isBlocked) {
      console.log('Permission Denied');
    } else {
      Mp3Recorder
        .start()
        .then(() => {
          this.setState({ isRecording: true });
        }).catch((e) => console.error(e));
    }
  };

  stop = () => {
    Mp3Recorder
      .stop()
      .getMp3()
      .then(([buffer, blob]) => {
        const blobURL = URL.createObjectURL(blob)
        this.setState({ blobURL, isRecording: false });
      }).catch((e) => console.log(e));
  };

  submit = async () => {
    let temp;
    var myBlob;
    //let blob = await fetch(this.state.blobURL).then(r => r.blob()).then(console.log);
    /*var xhr = new XMLHttpRequest();
      xhr.open('GET', this.state.blobURL, true);
      xhr.responseType = 'blob';
      xhr.onload = function(e) {
        if (this.status == 200) {
          myBlob = this.response;
          console.log("success");
    // myBlob is now the blob that the object URL pointed to.
    }
    else {
      console.log("failed");
    }
};
    await xhr.send();*/
    /*.then(blobFile => temp = new File([blobFile], "temp", { type: "audio/mp3" })).then(console.log);*/
    //var form = new FormData();
    //form.append('form', blob);
    let blob = await fetch(this.state.blobURL).then(r => r.blob());

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

          fetch("https://a2ec1528d7e7.ngrok.io/process-audio", requestOptions)
          .then(response => response.text())
          .then(result => console.log(result))
          .catch(error => console.log('error', error));
        }
      }
      startRecording = () => {
          this.setState({
            record: true
          });
        }

        stopRecording = () => {
          this.setState({
            record: false
          });
        }

        onData(recordedBlob) {
          console.log('chunk of real-time data is: ', recordedBlob);
        }

        onStop(recordedBlob) {
          console.log('recordedBlob is: ', recordedBlob);
        }


  componentDidMount() {
    navigator.getUserMedia({ audio: true },
      () => {
        console.log('Permission Granted');
        this.setState({ isBlocked: false });
      },
      () => {
        console.log('Permission Denied');
        this.setState({ isBlocked: true })
      },
    );
  }

  render(){
    return (
      <div className="Recorder">
          <button onClick={this.start} disabled={this.state.isRecording}>Record</button>
          <button onClick={this.stop} disabled={!this.state.isRecording}>Stop</button>
          <button onClick={this.submit} disabled={this.state.isRecording}> Submit</button>
          <audio src={this.state.blobURL} controls="controls" />


          <div>
          REACT-Mic
          </div>
          <div>
          <ReactMic
          record={this.state.record}
          className="sound-wave"
          onStop={this.onStop}
          onData={this.onData}
          strokeColor="#000000"
          backgroundColor="#FF4081" />
        <button onTouchTap={this.startRecording} type="button">Start</button>
        <button onTouchTap={this.stopRecording} type="button">Stop</button>
        </div>
      </div>
    );
  }
}

export default WebRecorder;
