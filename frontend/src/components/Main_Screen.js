/* eslint-disable jsx-a11y/anchor-has-content */
import React from 'react';
import cn from 'classnames';
import * as functions from './functions'

import styles from './Main_Screen.module.scss';

export default function Main_Screen(props) {

  const imgToRotate=cn(styles.block9, styles.block9_layout)

  return (
    <div className={`main--screen ${cn(styles.block, styles.block_layout)}`}>
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
              <div onClick={() => window.open('About ', '_self')} id={'aboutBtn'} className={cn(styles.block4, styles.block4_layout)}>
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

      <h1 id={'bestMoveText'} className={cn(styles.big_title, styles.big_title_layout)}>
      {'Next Best Move TextLabel'}
      </h1>

      <div className={cn(styles.block7, styles.block7_layout)}>
        <div className={cn(styles.block7_item)}>
          <div className={cn(styles.block8, styles.block8_layout)}>
            <div className={cn(styles.block8_item)}>
              <div
                style={{ '--src': `url(${require('assets/c18367ef261ee28362b173d7696e662f.png').default})` }}
                className={cn(styles.block9, styles.block9_layout)}
              />
            </div>
            <div className={cn(styles.block8_spacer)} />
            <div className={cn(styles.block8_item)}>
              <div
                style={{ '--src': `url(${require('assets/e485d7b3f099e5cf261cf7d8054518f1.png').default})` }}
                className={imgToRotate}
              />
            </div>
          </div>
        </div>
        <div className={cn(styles.block7_spacer)} />
        <div className={cn(styles.block7_item1)}>
          <div className={cn(styles.block10, styles.block10_layout)}>
            <h5 className={cn(styles.highlights_box, styles.highlights_box_layout)}>
              <pre className={cn(styles.highlights)}>{'Active  Colour'}</pre>
            </h5>

            <div className={cn(styles.block11, styles.block11_layout)} onClick={() => alert('ur gay')}>
              <div className={cn(styles.small_text_body, styles.small_text_body_layout)}>{'White to move'}</div>
            </div>

            <div className={cn(styles.block12, styles.block12_layout)} onClick={() => alert('ur gay')}>
              <div className={cn(styles.small_text_body, styles.small_text_body_layout)}>{'Black to move'}</div>
            </div>

            <div className={cn(styles.block13, styles.block13_layout)}>
              <div
                style={{ '--src': `url(${require('assets/7e4bc12a8d0425a844adbf6851effb40.png').default})` }}
                className={cn(styles.image3, styles.image3_layout)}
              />
              <div className={cn(styles.small_text_body1, styles.small_text_body1_layout)}>{'AI is thinking'}</div>
            </div>

            <div className={cn(styles.block14, styles.block14_layout)}>
              <div className={cn(styles.block15, styles.block15_layout)}>
                {/* When button clicked below, rotate className:imgToRotate */}
                <div className={cn(styles.block16, styles.block16_layout)} onClick={() => alert('ur gay')}> 
                  <div className={cn(styles.block16_item)}>
                    <div
                      style={{ '--src': `url(${require('assets/38c1e2e66d40992c6abb0c7ba136f929.png').default})` }}
                      className={cn(styles.icon1, styles.icon1_layout)}
                    />
                  </div>
                  <div className={cn(styles.block16_spacer)} />
                  <div className={cn(styles.small_text_body11, styles.small_text_body11_layout)}>{'Rotate Board'}</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

Main_Screen.inStorybook = true;
