using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System;

[System.Serializable]
public class PIDController : MonoBehaviour {

    [Tooltip("Proportional constant (counters current error)")]
    [SerializeField] private float Kp = 20f; // 67

    [Tooltip("Integral constant (counters cumulated error)")]
    [SerializeField] private float Ki = 1; //14

    [Tooltip("Derivative constant (fights oscillation)")]
    [SerializeField] private float Kd = 5f; //125

    [Tooltip("Current control value")]
    [SerializeField] private float value = 0;

    private float errorPrior = 0;
    private float integral = 0;

    // Use this for initialization
    void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    public float Update(float error)
    {
        return Update(error, Time.deltaTime);
    }

    /// 
    /// Update our value, based on the given error, which was last updated
    /// dt seconds ago.
    /// 
    /// <param name="error" />Difference between current and desired outcome.
    /// <param name="dt" />Time step.
    /// Updated control value.
    public float Update(float error, float dt)
    {
        float derivative = (error - errorPrior) / dt;
        integral += error * dt;
        errorPrior = error;

        value = Kp * error + Ki * integral + Kd * derivative;
        Debug.Log("Integral = " + integral + "\tErrorPrior = " + errorPrior + "\tValue = " + value);
        return value;
    }

    public void reset()
    {
        errorPrior = 0;
        integral = 0;
        value = 0;
    }


}
