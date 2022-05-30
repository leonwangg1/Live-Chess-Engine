/* eslint-disable jsx-a11y/anchor-has-content */
import React from 'react'
import cn from 'classnames';
import styles from './Main_Screen.module.scss';

function Contact(){
    return (
    <div className={`contact--screen ${cn(styles.block, styles.block_layout)}`}>
    <div className={cn(styles.block1, styles.block1_layout)}>
        <div className={cn(styles.block1_item)}>
          <a
            style={{ '--src': `url(${require('assets/c23ad5ef34005ba351c93eaa048f7182.png').default})` }}
            href="Main_Screen"
            onClick={() => window.open('Main_Screen', '_self')}
            className={cn(styles.image, styles.image_layout)}
          />
        </div>
        <div className={cn(styles.block1_spacer)} />
        <div className={cn(styles.block1_item1)}>
          <div className={cn(styles.block2, styles.block2_layout)}>
            <div className={cn(styles.block2_item)}>
              <div onClick={() => window.open('Main_Screen', '_self')} id={'chessBtn'} className={cn(styles.block3, styles.block3_layout)}>
                <div className={cn(styles.block3_item)}>
                  <div style={{ '--src': `url(${require('assets/3ad01d7c655419d658d998ab834b6e46.png').default})` }} className={cn(styles.icon, styles.icon_layout)} />
                </div>
                <h3 className={cn(styles.subtitle, styles.subtitle_layout)}>
                  {'Chess'}
                </h3>
              </div>
            </div>
            <div className={cn(styles.block2_spacer)} />
            <div className={cn(styles.block2_item1)}>
              <div onClick={() => window.open('About', '_self')} id={'aboutBtn'} className={cn(styles.block4, styles.block4_layout)}>
                <div className={cn(styles.block4_item)}>
                  <div className={cn(styles.block5, styles.block5_layout)}>
                    <div style={{ '--src': `url(${require('assets/cde979ed7f951020a3e3728f2640fd68.png').default})` }} className={cn(styles.image1, styles.image1_layout)} />
                  </div>
                </div>
                <h3 className={cn(styles.subtitle, styles.subtitle_layout1)}>
                  {'About'}
                </h3>
              </div>
            </div>
            <div className={cn(styles.block2_spacer1)} />
            <div className={cn(styles.block2_item2)}>
              <div onClick={() => window.open('Contact', '_self')} id={'contactBtn'} className={cn(styles.block6, styles.block6_layout)}>
                <div className={cn(styles.block6_item)}>
                  <div className={cn(styles.block5, styles.block5_layout)}>
                    <div style={{ '--src': `url(${require('assets/5b12e2e5b7b048cf0fc3341616c96099.png').default})` }} className={cn(styles.image1, styles.image1_layout)} />
                  </div>
                </div>
                <h3 className={cn(styles.subtitle, styles.subtitle_layout2)}>
                  {'Contact'}
                </h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    );
}

export default Contact;