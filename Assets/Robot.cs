using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Robot : MonoBehaviour
{
    Robot robot;
    public float targetRotation = 2f;
    public PIDController pid;
    public Rigidbody rigidBody;

    [SerializeField] float mainThrust = 100f;

    // Start is called before the first frame update
    void Start()
    {
        robot = GetComponent<Robot>();
        rigidBody = GetComponent<Rigidbody>();
    }

    // Update is called once per frame
    void Update()
    {
       // BalanceRobot();
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
        //float currentAltitude = 1f;
        //float error = targetAltitude - currentAltitude;
        //if (transform.rotation.eulerAngles.z > 0)
        //    rigidbody.AddRelativeTorque(-transform.forward * pid.Update(error) * transform.rotation.eulerAngles.z);

        //if (transform.rotation.eulerAngles.z < 0)
        //    rigidbody.AddRelativeTorque(transform.forward * pid.Update(error) * -(transform.rotation.eulerAngles.z - 360));
  
        //Mathf.Clamp01(pid.Update(error))
        //rigidBody.AddForce(Vector3.forward * Time.deltaTime * 100);
    }
}


