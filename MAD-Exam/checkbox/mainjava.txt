package com.example.radiocheckbox;

import android.os.Bundle;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button submit;

    RadioGroup rg;
    RadioButton male, female;

    CheckBox english, malayalam, hindi;

    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        // Connect Java variables with XML views

        submit = findViewById(R.id.submit);

        rg = findViewById(R.id.rg);

        male = findViewById(R.id.male);
        female = findViewById(R.id.female);

        english = findViewById(R.id.e);
        malayalam = findViewById(R.id.m);
        hindi = findViewById(R.id.h);

        tv = findViewById(R.id.tv);

        // Radio button selection

        rg.setOnCheckedChangeListener(
                new RadioGroup.OnCheckedChangeListener() {

                    @Override
                    public void onCheckedChanged(
                            RadioGroup group, int checkedId) {

                        RadioButton selected =
                                findViewById(checkedId);

                        Toast.makeText(
                                MainActivity.this,
                                "Selected: " + selected.getText(),
                                Toast.LENGTH_SHORT
                        ).show();
                    }
                });

        // Submit button

        submit.setOnClickListener(v -> {

            String result = "Languages Known:\n";

            if (english.isChecked()) {
                result += "English\n";
            }

            if (malayalam.isChecked()) {
                result += "Malayalam\n";
            }

            if (hindi.isChecked()) {
                result += "Hindi\n";
            }

            tv.setText(result);
        });
    }
}