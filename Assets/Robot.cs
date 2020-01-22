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
    public Vector3 originalPosition;
    public Quaternion originalRotation;
    [SerializeField] float mainThrust = 100f;
    // rotation z;
    // Start is called before the first frame update
    void Start()
    {
        initializeVariables();
    }

    void initializeVariables()
    {
        robot = GetComponent<Robot>();
        rigidBody = GetComponent<Rigidbody>();
        originalPosition = new Vector3(rigidBody.transform.position.x, rigidBody.transform.position.y, rigidBody.transform.position.z);
        originalRotation = Quaternion.Euler(rigidBody.transform.rotation.x, -90, rigidBody.transform.rotation.z);
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
        if (Input.GetKey(KeyCode.R))
        {
            //rigidBody.transform.position = originalPosition;
            //rigidBody.transform.rotation = Quaternion.identity;

            resetPosition();
            resetRotation();
            pid.reset();
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
        if (transform.rotation.eulerAngles.z >= 0)
        {
            GetComponent<Rigidbody>().AddTorque(-transform.forward * pid.Update(error) * transform.rotation.eulerAngles.z);

            //rigidBody.AddTorque(-transform.forward * pid.Update(error) * transform.rotation.eulerAngles.z);

            Debug.Log("Balance Robot in > 0");
        }
        //rigidBody.AddForce(Vector3.forward * Time.deltaTime * 10);
    }

    private void resetWhenBalanceLost()
    {
        if (rigidBody.transform.position.x < 0 || rigidBody.transform.position.y < 0)
        {
            resetPosition();
            resetRotation();
            pid.reset();
        }
    }

    private void resetPosition()
    {
        rigidBody.transform.position = Vector3.zero;
    }

    private void resetRotation()
    {
        rigidBody.transform.rotation = originalRotation;
    }
}



