### 根据平台 组件放在不同的文件夹下
/common/components
/android/components
/ios/components

或者
bigButtonIOS.js
bigButtonAndroid.js


### 扩展名不同
bigButton.ios.js
bigButton.android.js

引用时 require('./components/bigButton'); 自动加载符合当前平台的组件


### Platform.Version
import {Platform} from 'react'

if(Platform.Version == 21){
    console.log('running on lollipop!');
} 

