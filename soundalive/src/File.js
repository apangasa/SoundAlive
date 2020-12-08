import React from 'react';
import FileBase64 from 'react-file-base64';



export default class File extends React.Component {
//state holds files
  constructor(props) {
    super(props)
    this.state = {
      files: [],
      //to implement set loading to true and display loading image
      loading: false,
    }
  }
  extractResult(result) {
    //set of possible animals constructed from tree results
    let set = new Set();
    result.Splay.matches.forEach(element =>
      set.add(element)
    );
    result.B.matches.forEach(element =>
      set.add(element)
    );
    //remove user displayed setAnimal
    set.delete(result.Splay.matches[0]);
    //passes data to App.js
    this.props.onFileSend(result.Splay.matches[0], result.B.time, result.Splay.time, set);
  }
  // Callback to get files and perform request to server
  getFiles(files){
    this.setState({ files: files });
    this.setState({ loading: true })
    console.log(files.name.split(".")[0]);
    console.log(files.base64);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    //sending file base64 encoded to backend
    var raw = JSON.stringify({"content":files.base64, "filename": files.name.split(".")[0]});
    var requestOptions = {
          method: 'POST',
          headers: myHeaders,
          body: raw,
          redirect: 'follow'
        };
        //request to send file data
        fetch("https://apangasa.pythonanywhere.com/process-audio", requestOptions)
        .then(response => response.json())
        .then(result =>
          this.extractResult(result)
        )
        .catch(error => console.log('error', error));
  }

  render() {
    //if no file allow upload
    if (!this.state.loading){
      return (

      <FileBase64
        multiple={ false }
        onDone={ this.getFiles.bind(this) } />

    )}
    else {
      //loading response
      return (
        <p> Loading </p>
      )
    }
  }

}
