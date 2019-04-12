import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text } from 'react-native';
import { strings } from '../src/i18n';

export default class AllReceipsScreen extends React.Component {
  
  constructor(props) {
    super(props);
  }
  static navigationOptions = {
    title: 'Tutte le ricette',
  };

  render() {

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        paddingTop: 15,
        backgroundColor: '#fff',
      },
    });

    return  <View style={styles.container}>
              <Text>{strings('ReceipsNav.titleAllReceips')}</Text> 
            </View>  
    }    
}
