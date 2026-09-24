package com.example.checkbox;

import android.os.Bundle;
import android.view.View;
import android.widget.*;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    RadioGroup rg;
    CheckBox e, m, h;
    Button submit;
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        rg = findViewById(R.id.rg);
        e = findViewById(R.id.e);
        m = findViewById(R.id.m);
        h = findViewById(R.id.h);
        submit = findViewById(R.id.submit);
        tv = findViewById(R.id.tv);

        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                tv.setText("Languages Known:");

                if (e.isChecked())
                    tv.append(" English");

                if (m.isChecked())
                    tv.append(" Malayalam");

                if (h.isChecked())
                    tv.append(" Hindi");
            }
        });

        rg.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int id) {

                RadioButton r = findViewById(id);

                Toast.makeText(MainActivity.this,
                        r.getText(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}