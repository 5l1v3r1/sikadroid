/*
 * Copyright (c) 2012 Archzilon Eshun-Davies <laudarch@qremiaevolution.org>
 *
 * Permission to use, copy, modify, and distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */
package org.qremiaevolution.sika;

import android.app.Activity;
import android.content.res.Configuration;
import android.os.Bundle;
import android.view.*;
import android.webkit.WebView;
//import android.widget.*;

/**
 * Sika Droid Activity
 * 
 */
public class SikaDroid extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        
        requestWindowFeature(Window.FEATURE_NO_TITLE);

        WebView webview = new WebView(this);
        setContentView(webview);

        webview.getSettings().setJavaScriptEnabled(true);
        webview.getSettings().setPluginsEnabled(false);
        webview.loadUrl("file:///android_asset/www/index.html");
    }
    
    /**
     * Configuration Change detection
     */
    @Override
    public void onConfigurationChanged(Configuration newConfig)
    {
        super.onConfigurationChanged(newConfig);

        if (newConfig.orientation == Configuration.ORIENTATION_LANDSCAPE) {
            //Toast.makeText(this, "landscape", Toast.LENGTH_SHORT).show();
        } else if (newConfig.orientation == Configuration.ORIENTATION_PORTRAIT){
            //Toast.makeText(this, "portrait", Toast.LENGTH_SHORT).show();
        }
      }

    /**
     * Prevent back button :)
     * 
     */
    @Override
	public boolean onKeyDown(int keyCode, KeyEvent event)
	{
		if ((keyCode == 0x00000004) || (keyCode == 0x0000001a)) {
			quit();
			return (true);
		} else
			return (false);
	}
    
   @Override
    public void onPause()
   {
    	super.onPause();
    }
    
    @Override
    public void onResume() 
    {
    	super.onResume();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu)
    {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item)
    {
        switch (item.getItemId()) {
        case R.id.exit:
            quit();
            return (true);
        default:
            return super.onOptionsItemSelected(item);
        }
    }

    @Override
	public void onDestroy()
	{
    	super.onDestroy();
		quit();
	}

    /**
     * Quit function
     * 
     */
    private void quit()
    {
        finish();
        System.exit(0);
    }
}