import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text, ScrollView, Button } from 'react-native';
import { strings } from '../src/i18n';
import AlphabetListView from 'react-native-alphabetlistview'
export default class AllReceipsScreen extends React.Component {

  constructor(){
    super();
    this.state = {data: null}
    this.getReceips();
  }

  static navigationOptions = {
    title: 'Tutte le ricette',
  };

  async getReceips(){

    await fetch('http://192.168.1.53:8080/receips/', {
         method: 'GET'
    })
    .then((response) => {
      return response.json()
    })
    .then((responseJson) => {
        this.setState({
          data: JSON.parse(responseJson)
        })
      // console.log(this.state.data)
    })
    .catch((error) => {
        console.error(error);
    })

  }



  render() {

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        paddingTop: 15,
        backgroundColor: '#fff',
      },
    });
    var receipsList = []
    
    if (this.state.data === null || this.state.data === undefined ){
      
      return <View style={styles.container}>
              <Text> Loading Receips.. {typeof(this.state.data)} </Text>
            </View> 
    }
    for(i = 0; i < 10000; i++){
        receipsList.push(<Button title={this.state.data[i].name}/>)
    }

    // receipsList = this.state.data.map((item) =>
    //   <Button onPress={this._onPress} title={item.name} color="#FFFFFF" accessibilityLabel="Tap on Me"/>)
    return    <View style={styles.buttonContainer}>                  
                  <ScrollView> 
                    {receipsList}          
                  {/* <AlphabetListView
                    data={this.state.data}
                    cell={Cell}
                    cellHeight={30}
                    sectionListItem={SectionItem}
                    sectionHeader={SectionHeader}
                    sectionHeaderHeight={22.5}
                  />  */}
                  </ScrollView>              
              </View>             
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFFFFF'
  },
  buttonContainer: {
    backgroundColor: '#2E9298',
    borderRadius: 10,
    padding: 10,
    shadowColor: '#000000',
    shadowOffset: {
      width: 0,
      height: 3
    },
    shadowRadius: 10,
    shadowOpacity: 0.25
  }
})

// class SectionHeader extends React.Component {
//   render() {
//     // inline styles used for brevity, use a stylesheet when possible
//     var textStyle = {
//       textAlign:'center',
//       color:'#fff',
//       fontWeight:'700',
//       fontSize:16
//     };

//     var viewStyle = {
//       backgroundColor: '#ccc'
//     };
//     // console.log("section "+ this.props)
//     return (
//       <View style={viewStyle}>
//         <Text style={textStyle}>{this.props.title}</Text>
//       </View>
//     );
//   }
// }

// class SectionItem extends React.Component {
//   render() {
//     // console.log("item "+this.props)
//     return (
//       <Text style={{color:'#f00'}}>{this.props.title}</Text>
//     );
//   }
// }

// class Cell extends React.Component {
//   render() {
//     //console.log("Cell "+this.props)
//     return (
//       <View style={{height:30}}>
//         <Text>{this.props.item}</Text>
//       </View>
//     );
//   }
// }

