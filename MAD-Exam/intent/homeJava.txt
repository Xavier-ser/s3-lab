package com.example.intentdemo;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class Homepage extends AppCompatActivity {

    TextView txt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_homepage);

        txt = findViewById(R.id.txt);

        String name =
                getIntent().getStringExtra("username");

        txt.setText("Welcome " + name);
    }
}