package com.example.studentmarks;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    EditText name, internal, external;
    Button saveButton, viewButton;
    SharedPreferences preferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        name = findViewById(R.id.name);
        internal = findViewById(R.id.internal);
        external = findViewById(R.id.external);

        saveButton = findViewById(R.id.saveButton);
        viewButton = findViewById(R.id.viewButton);

        // Create SharedPreferences
        preferences = getSharedPreferences(
                "StudentData",
                MODE_PRIVATE
        );




        saveButton.setOnClickListener(v -> saveStudent());

        viewButton.setOnClickListener(v -> {

            Intent intent = new Intent(
                    MainActivity.this,
                    ViewMarksActivity.class
            );

            startActivity(intent);
        });

    }


    private void saveStudent() {

        String studentName =
                name.getText().toString().trim();

        String internalMarks =
                internal.getText().toString().trim();

        String externalMarks =
                external.getText().toString().trim();

        if (studentName.isEmpty() ||
                internalMarks.isEmpty() ||
                externalMarks.isEmpty()) {

            Toast.makeText(
                    this,
                    "Enter all details",
                    Toast.LENGTH_SHORT
            ).show();

            return;
        }


        // Get existing number of students
        int count = preferences.getInt("count", 0);

        // Save student using a unique key
        SharedPreferences.Editor editor = preferences.edit();

        editor.putString(
                "name_" + count,
                studentName
        );

        editor.putString(
                "internal_" + count,
                internalMarks
        );

        editor.putString(
                "external_" + count,
                externalMarks
        );

        // Increase student count
        editor.putInt("count", count + 1);

        editor.apply();

        Toast.makeText(
                this,
                "Student saved successfully",
                Toast.LENGTH_SHORT
        ).show();

        // Clear input fields
        name.setText("");
        internal.setText("");
        external.setText("");
    }
}