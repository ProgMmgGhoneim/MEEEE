import React ,{Component} from 'react';
import axios from 'axios';

import Articles from './Articles';

const listData = [];
for (let i = 0; i < 23; i++) {
    listData.push({
    href: 'http://ant.design',
    title: `ant design part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    });
}


class ArticleList extends Component {
  state ={
    atricle :[]
  }
  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/')
    .then(res =>{
      this.setState({
        article :res.data
      });
      console.log(res.data)
    })
  }
  render(){
    return(
    <div>
    <Articles data={this.state.article}/>
    </div>
);
  }
}

export default ArticleList;