package com.example.intentdemo;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText user, pass;
    Button login;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        user = findViewById(R.id.user);
        pass = findViewById(R.id.pass);
        login = findViewById(R.id.login);

        login.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                String u = user.getText().toString();
                String p = pass.getText().toString();

                if (u.equals("admin") && p.equals("123")) {

                    Intent i =
                            new Intent(MainActivity.this,
                                    Homepage.class);

                    i.putExtra("username", u);

                    startActivity(i);

                } else {

                    Toast.makeText(
                            MainActivity.this,
                            "Invalid Login",
                            Toast.LENGTH_SHORT
                    ).show();
                }
            }
        });
    }
}