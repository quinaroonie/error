import * as React from 'react';
import { Socket } from './Socket';


export class Content extends React.Component {
  constructor(props){
        super(props);
    //Initial state is an array of empty messages
    this.state = {data_received: []};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleChange(event) {
    this.setState({value: event.target.value});
  }
  
  handleSubmit(event) {
      Socket.emit('message', 
      {'message':this.state.value,
    
      });
       console.log('User Message:', this.state.message);
      
      event.preventDefault();
      //      console.log(this.state.data_received);
      
     
  }

    componentDidMount() {
        Socket.on('message received', (data) => {
            console.log("Content recieved message");
            this.setState({
                'number_received': data['message']
            });
        });
    }

    render() {
        let new_message = this.state.data_received;
        
        return (
            <div1 style={{backgroundColor: '#ffe680', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
            <h1>CHATROOM</h1>
            <h2> USERNAME </h2>
            
            <div2 style={{backgroundColor: 'white', position: 'absolute', left: '5%', width: '150px', height: '300px', border: '1px solid #000'}}> 
            
            <form2> {new_message} </form2>
            
            </div2>
            
            
            <div3 style={{backgroundColor: 'white', position: 'absolute', left: '30%', width: '400px', height: '300px', border: '1px solid #000'}}> 
              
            
             
        
            </div3>
                <form>
                <label style={{ color:'black' }}>
                
                <h3> ENTER USERNAME </h3>
                
                <input value={this.state.username} onChange={this.handleUsernameChange}/>
                
                
                
               <h4> MESSAGE</h4>
               
                <textarea value={this.state.value} onChange={this.handleChange} />
                </label>
              <h5>  
            <form1 onSubmit={this.handleSubmit}>
                <button>SEND</button>
            </form1>
                </h5>
                </form>
            
        </div1> ); 
    }
}