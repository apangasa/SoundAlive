import React from 'react';
import MicRecorder from 'mic-recorder-to-mp3';

const Mp3Recorder = new MicRecorder({ bitRate: 128 });

class WebRecorder extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      isRecording: false,
      blobURL: '',
      isBlocked: false,
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

  submit = () => {
    let blob = fetch(this.state.blobURL).then(r => r.blob()).then(console.log).then(blobFile => new File([blobFile], "temp", { type: "audio/mp3" })).then(console.log);
    //console.log(blob);
    fetch('https://48f2452b63c6.ngrok.io/process-audio', {
    method: 'post',
    body : {
    'content': blob},
  }
)
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

      </div>
    );
  }
}

export default WebRecorder;
