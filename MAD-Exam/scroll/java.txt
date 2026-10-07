package com.example.scrollviewdemo;

import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    LinearLayout container;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        container = findViewById(R.id.linearLayoutContainer);

        for (int i = 1; i <= 20; i++) {

            TextView tv = new TextView(this);

            tv.setText("TextView " + i);

            tv.setTextSize(30);

            tv.setPadding(20, 20, 20, 20);

            container.addView(tv);
        }
    }
}