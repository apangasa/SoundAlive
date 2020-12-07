import React from 'react';
import FileBase64 from 'react-file-base64';



export default class File extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      files: [],
      loading: false,
    }
  }
  extractResult(result) {
    let set = new Set();
    result.Splay.matches.forEach(element =>
      set.add(element)
    );
    result.B.matches.forEach(element =>
      set.add(element)
    );
    set.delete(result.Splay.matches[0]);
    this.props.onFileSend(result.Splay.matches[0], result.B.time, result.Splay.time, set);
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

        fetch("https://apangasa.pythonanywhere.com/process-audio", requestOptions)
        .then(response => response.json())
        .then(result =>
          this.extractResult(result)
        )
        .catch(error => console.log('error', error));
  }

  render() {
    if (!this.state.loading){
      return (

      <FileBase64
        multiple={ false }
        onDone={ this.getFiles.bind(this) } />

    )}
    else {
      return (
        <p> Loading </p>
      )
    }
  }

}
