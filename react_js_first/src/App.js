import React, { Component } from "react";
import ReactDOM from "react-dom";

class App extends Component {
  constructor() {
    super();
    this.state = { query: '',data: [], delete:false };
  }

  async fetch_tweet(q) {
    this.state.delete=false;
  console.log(q);
  const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 'query': q })
      };
    const response = await fetch('http://127.0.0.1:2000/get',requestOptions);
    const json = await response.json();
    this.setState({ data: json });
    console.log(json);
  }

  async post_tweet(tweet) {
  this.state.delete=false;
  console.log("tweet : ",tweet);
  const requestOptions = {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ 'tweet': tweet })
   };
   const response = await fetch('http://127.0.0.1:2000/post',requestOptions);
   console.log(response);
   alert("posted");
   this.my_tweet();
  }

  async delete_tweet(id) {
    this.state.delete=true;
    console.log("tweet : ",id);
    const requestOptions = {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 'twitter_id': id })
     };
     const response = await fetch('http://127.0.0.1:2000/delete',requestOptions);
     console.log(response);
     alert("deleted");
     this.my_tweet();
    }

  async my_tweet() {
    this.state.delete=true;
    const requestOptions = {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' }
    };
      const response = await fetch('http://127.0.0.1:2000/my_tweet',requestOptions);
      const json = await response.json();
      this.setState({ data: json });
      console.log("data: ",json);
    }

  render() {
    return (
      <div>
      <h1> Twitter assignment</h1>
        <input type="text" placeholder="Enter Text to Search/Tweet"
         aria-label="Search"
                                style = {{ width: '40%', float: 'left'}}
                                onChange={(event)=>{
                                    this.setState({
                                        query:event.target.value,
                                        type:true
                                    });
                                }}
                            />
        <button type="button" style = {{float: 'left', marginLeft: '2%'}}
                                onClick={() =>  this.fetch_tweet(this.state.query)}
                            >Search</button>
        <button type="button" style = {{float: 'left', marginLeft: '2%'}}
                                onClick={() =>  this.post_tweet(this.state.query)
                                }
                            >Tweet</button>
        <button type="button" style = {{float: 'left', marginLeft: '2%'}}
                                        onClick={() =>  this.my_tweet()
                                        }
                                    >My Tweets</button>
                            <br></br>
        <ul>
          {this.state.data.map(el => (
            <li key={el.tweet_id}>
              <ol>{el.tweet_id}</ol>
              <ol>{el.user_name}:</ol>
              <ol>{el.tweet}</ol>

              {this.state.delete === true && (
                    <button type="button" id="delete_btn"
                    style={{position: 'relative',float: 'right', margin: 'auto', }}
                    onClick = {
                       ()=>this.delete_tweet(el.tweet_id)
                    } >DELETE</button>
              )}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default App;
