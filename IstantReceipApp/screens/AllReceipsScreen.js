import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text, ScrollView } from 'react-native';
import { strings } from '../src/i18n';

export default class AllReceipsScreen extends React.Component {
  
  constructor(){
    super();
    this.state = {data: []}
    this.getReceips();
  }
    
  static navigationOptions = {
    title: 'Tutte le ricette',
  };

  async getReceips(){

    await fetch('http://192.168.1.12:8080/receips/', {
         method: 'GET',
         headers: {id: 2345}
    })
    .then((response) => 
      response.json())
    .then((responseJson) => {
        this.setState({
          data: responseJson            
        })
        console.log(this.state.data)
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
    if (this.state.data == null){
      console.log("ciao")
      return <View style={styles.container}></View>
    }else{
      console.log("OK")
      return  <View style={styles.container}>
                <ScrollView>
                  <Text>{strings('ReceipsNav.titleAllReceips')}</Text> 
                  <Text>{this.state.data}</Text>  
                </ScrollView>
              </View>
    }  
  }    
}
