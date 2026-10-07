package com.example.implicitintent;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button open;
    TextView result;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        open = findViewById(R.id.open);
        result = findViewById(R.id.result);

        open.setOnClickListener(v -> {

            Intent intent = new Intent(Intent.ACTION_VIEW);

            intent.setData(
                    Uri.parse("https://www.cet.ac.in")
            );

            startActivity(intent);

            result.setText("Website Opened");
        });
    }
}