import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text, ScrollView, Button } from 'react-native';
import { strings } from '../src/i18n';

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
    .then((response) => 
      response.json())
    .then((responseJson) => {
        this.setState({
          data: responseJson            
        })

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

    while (this.state.data === null || this.state.data === undefined )      
      return  <Text> Loading Receips.. {typeof(this.state.data)} </Text> 

    return  <View style={styles.container}>
              <Text> {typeof(this.state.data)} </Text>
              <Text> {this.state.data} </Text>
              <ScrollView>
                {receipsList}  
              </ScrollView>
            </View>
  } 
  
}
