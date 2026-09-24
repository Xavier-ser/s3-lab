package com.example.chwiggy;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText q1, q2, q3;
    Button btn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        q1 = findViewById(R.id.q1);
        q2 = findViewById(R.id.q2);
        q3 = findViewById(R.id.q3);

        btn = findViewById(R.id.btn);

        btn.setOnClickListener(v -> {

            int total = 0;

            if (!q1.getText().toString().isEmpty()) {
                int qty = Integer.parseInt(q1.getText().toString());
                total += qty * 150;
            }

            if (!q2.getText().toString().isEmpty()) {
                int qty = Integer.parseInt(q2.getText().toString());
                total += qty * 200;
            }

            if (!q3.getText().toString().isEmpty()) {
                int qty = Integer.parseInt(q3.getText().toString());
                total += qty * 250;
            }

            if (total == 0)
                Toast.makeText(this, "Select at least one item", Toast.LENGTH_SHORT).show();
            else
                Toast.makeText(this, "Total Cost: ₹" + total, Toast.LENGTH_SHORT).show();
        });
    }
}