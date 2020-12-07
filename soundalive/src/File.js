import React from 'react';
import FileBase64 from 'react-file-base64';

export default class File extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      files: []
    }
  }

  // Callback~
  getFiles(files){
    this.setState({ files: files })
    console.log(files.base64);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({"content":files.base64});

      var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };

        fetch("https://70b6fcf64826.ngrok.io/process-audio", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .then(this.props.onFileSend("animal", "time"))
        .catch(error => console.log('error', error));
  }

  render() {
    return (
      <FileBase64
        multiple={ false }
        onDone={ this.getFiles.bind(this) } />
    )
  }

}
