import React from 'react';
import { Platform, StatusBar, StyleSheet, View, Text } from 'react-native';
import { strings } from '../src/i18n';

export default class SpecialReceipsScreen extends React.Component {
  static navigationOptions = {
    title: 'Ricette Special',
  };
  constructor(props) {
    super(props);
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
              <Text>{strings('ReceipsNav.titleSpecialResearch')}</Text> 
            </View>  
    }    
}
