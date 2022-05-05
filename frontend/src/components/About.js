import React from 'react'
import styles from './Main_Screen.module.scss';
import cn from 'classnames';

function About(){
    return (
        <div style={{ '--src': `url(${require('assets/5yrbtx.png').default})` }} className={cn(styles.block9, styles.block9_layout)} />
    );
}

export default About;