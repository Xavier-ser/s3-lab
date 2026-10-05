package com.example.activitylifecycle;

import android.os.Bundle;
import android.util.Log;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        Log.d("Appstate", "onCreate");
    }

    @Override
    protected void onStart() {
        super.onStart();

        Log.d("Appstate", "onStart");
    }

    @Override
    protected void onResume() {
        super.onResume();

        Log.d("Appstate", "onResume");
    }

    @Override
    protected void onPause() {
        super.onPause();

        Log.d("Appstate", "onPause");
    }

    @Override
    protected void onStop() {
        super.onStop();

        Log.d("Appstate", "onStop");
    }

    @Override
    protected void onRestart() {
        super.onRestart();

        Log.d("Appstate", "onRestart");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();

        Log.d("Appstate", "onDestroy");
    }
}