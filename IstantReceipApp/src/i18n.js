import ReactNative from 'react-native';
import I18n from 'react-native-i18n';

// Import all locales
import en from '../locales/en.json';
import it from '../locales/it.json';
import { Localization } from 'expo';

// Should the app fallback to English if user locale doesn't exists
I18n.fallbacks = true;

// Define the supported translations
I18n.translations = {
  en,
  it,
}; 

const curr = I18n.locale
const currentLocale = I18n.currentLocale();
console.log(curr)
console.log(currentLocale)
// Is it a RTL language?
export const isRTL = currentLocale.indexOf('en') === 0 || currentLocale.indexOf('ar') === 0;
import { NativeModules } from 'react-native';
const { RNI18n } = NativeModules;

console.log(RNI18n)
// Allow RTL alignment in RTL languages
ReactNative.I18nManager.allowRTL(isRTL);

// The method we'll use instead of a regular string
export function strings(name, params = {}) {
  return I18n.t(name, params);
};

export default I18n;