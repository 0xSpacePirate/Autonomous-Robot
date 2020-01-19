using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Robot : MonoBehaviour
{
    Robot robot;
    public float targetAltitude = -1f;
    public PIDController pid;
    public Rigidbody rigidBody;

    [SerializeField] float mainThrust = 100f;
    // rotation z;
    // Start is called before the first frame update
    void Start()
    {
        robot = GetComponent<Robot>();
        rigidBody = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
        BalanceRobot();
        RespondToInput();
    }

    private void RespondToInput()
    {
        if (Input.GetKey(KeyCode.W))
        {
            transform.Translate(Vector3.left * Time.deltaTime);
        }
        if (Input.GetKey(KeyCode.S))
        {
            transform.Translate(Vector3.right * Time.deltaTime);
        }
    }

    private void BalanceRobot()
    {
        float currentAltitude = transform.position.z;
        float error = -currentAltitude;
        Debug.Log("Error=" + error);
        Debug.Log(transform.rotation.eulerAngles.z + " - " + 360 + " = " + (-(transform.rotation.eulerAngles.z - 360)));

        //falling forward;
        if (transform.rotation.eulerAngles.z < 0)
        {
            GetComponent<Rigidbody>().AddTorque(transform.forward * pid.Update(error) * -(transform.rotation.eulerAngles.z - 360));
            Debug.Log("Balance Robot in < 0");
        }

        //falling backwards
        if (transform.rotation.eulerAngles.z > 0)
        {
            GetComponent<Rigidbody>().AddTorque(-transform.forward * pid.Update(error) * transform.rotation.eulerAngles.z);

            //rigidBody.AddTorque(-transform.forward * pid.Update(error) * transform.rotation.eulerAngles.z);

            Debug.Log("Balance Robot in > 0");
        }
        //rigidBody.AddForce(Vector3.forward * Time.deltaTime * 10);
    }
}


