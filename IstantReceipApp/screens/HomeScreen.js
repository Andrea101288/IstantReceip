// import React from 'react';
// import {
//   ImageBackground,
//   Image,
//   Platform,
//   ScrollView,
//   StyleSheet,
//   Text,
//   TouchableOpacity,
//   View,
//   Dimensions,
//   Button,
// } from 'react-native';
// import {Content} from 'native-base';
// import { WebBrowser } from 'expo';

// export default class HomeScreen extends React.Component {
//   static navigationOptions = {
//     header: null,
//   };

//   constructor(props) {
//     super(props);
//   };
  
//   render() {
//     const {width, height} = Dimensions.get("window")
//     const { navigate } = this.props.navigation
//     console.log(navigate)
//     return (
//       <View style={styles.container}>                   
//           <ImageBackground style={{height: height, width:width }} 
//             resizeMode='contain' 
//             source={require('../assets/images/IRBack.png')}>
//             <View>
//               <Button style={styles.button}
//                 onPress={() => navigate('ReceipsScreen')}
//                 title="ALL THE RECEIPS"
//                 color="#841584"
//             />
//             </View>
//           </ImageBackground>         
//       </View>
//     );
//   }

//   _maybeRenderDevelopmentModeWarning() {
//     if (__DEV__) {
//       const learnMoreButton = (
//         <Text onPress={this._handleLearnMorePress} style={styles.helpLinkText}>
//           Learn more
//         </Text>
//       );

//       return (
//         <Text style={styles.developmentModeText}>
//           Development mode is enabled, your app will be slower but you can use useful development
//           tools. {learnMoreButton}
//         </Text>
//       );
//     } else {
//       return (
//         <Text style={styles.developmentModeText}>
//           You are not in development mode, your app will run at full speed.
//         </Text>
//       );
//     }
//   }

//   _handleLearnMorePress = () => {
//     WebBrowser.openBrowserAsync('https://docs.expo.io/versions/latest/guides/development-mode');
//   };

//   _handleHelpPress = () => {
//     WebBrowser.openBrowserAsync(
//       'https://docs.expo.io/versions/latest/guides/up-and-running.html#can-t-see-your-changes'
//     );
//   };
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//   },
//   developmentModeText: {
//     marginBottom: 20,
//     color: 'rgba(0,0,0,0.4)',
//     fontSize: 14,
//     lineHeight: 19,
//     textAlign: 'center',
//   },
//   contentContainer: {
//     paddingTop: 30,
//   },
//   welcomeContainer: {
//     alignItems: 'center',
//     marginTop: 10,
//     marginBottom: 20,
//   },
//   welcomeImage: {
//     width: 100,
//     height: 80,
//     resizeMode: 'contain',
//     marginTop: 3,
//     marginLeft: -10,
//   },
//   getStartedContainer: {
//     alignItems: 'center',
//     marginHorizontal: 50,
//   },
//   homeScreenFilename: {
//     marginVertical: 7,
//   },
//   codeHighlightText: {
//     color: 'rgba(96,100,109, 0.8)',
//   },
//   codeHighlightContainer: {
//     backgroundColor: 'rgba(0,0,0,0.05)',
//     borderRadius: 3,
//     paddingHorizontal: 4,
//   },
//   getStartedText: {
//     fontSize: 17,
//     color: 'rgba(96,100,109, 1)',
//     lineHeight: 24,
//     textAlign: 'center',
//   },
//   tabBarInfoContainer: {
//     position: 'absolute',
//     bottom: 0,
//     left: 0,
//     right: 0,
//     ...Platform.select({
//       ios: {
//         shadowColor: 'black',
//         shadowOffset: { height: -3 },
//         shadowOpacity: 0.1,
//         shadowRadius: 3,
//       },
//       android: {
//         elevation: 20,
//       },
//     }),
//     alignItems: 'center',
//     backgroundColor: '#fbfbfb',
//     paddingVertical: 20,
//   },
//   tabBarInfoText: {
//     fontSize: 17,
//     color: 'rgba(96,100,109, 1)',
//     textAlign: 'center',
//   },
//   navigationFilename: {
//     marginTop: 5,
//   },
//   helpContainer: {
//     marginTop: 15,
//     alignItems: 'center',
//   },
//   helpLink: {
//     paddingVertical: 15,
//   },
//   helpLinkText: {
//     fontSize: 14,
//     color: '#2e78b7',
//   },
//   button: {
//     alignItems: 'center',
//     backgroundColor: '#DDDDDD',
//     flex: 1,
//   },  
//   imgBackground: {
//     width: 20,
//     height: 20,
//     flex: 1
//   },
// });
import React from 'react';

import {

  Platform,
  Image,
  View,
  Text,
  AsyncStorage,
  BackHandler,
  StyleSheet,

} from 'react-native';
import { createMaterialTopTabNavigator } from 'react-navigation';
import Screen1 from '../screens/AllReceipsScreen';
import Screen2 from '../screens/SpecialReceipsScreen';
import Screen3 from '../screens/StandardReceipsScreen';



const MyNavigator = createMaterialTopTabNavigator(
  {
    Screen1,
    Screen2,
    Screen3,
  },
  {
    navigationOptions: ({ navigation, screenProps }) => ({
      header: null,
      headerMode: 'none',
      tabBarVisible: true,
      tabBarLabel: () => {
        const { routeName } = navigation.state;
        switch (routeName) {
          //
        }
        return <Text>{routeName}</Text>;
      },
    }),
    animationEnabled: false,
    swipeEnabled: true,
    tabBarOptions: {
      activeTintColor: 'rgb(12,157,197)',
      inactiveTintColor: 'black',
      indicatorStyle: {
        backgroundColor: 'rgb(102,134,205)',
      },
      labelStyle: {
        fontSize: 14 /2,
        color: 'tomato',
      },
      tabStyle: {
        height: 48,
        alignItems: 'center',
        justifyContent: 'center',
      },
      style: {
        backgroundColor: 'white',
      },
      statusBarStyle: 'light-content',
    },
  },
);
class Page extends React.Component {
  static router = MyNavigator.router;
  
  constructor(){
    super();

    fetch('http://192.168.1.12:8080/ingredients/', {
         method: 'GET',
         headers: {id: 2345}
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
    return (
      <MyNavigator
        navigation={this.props.navigation}        
      />
    );
  }
}
export default Page;
