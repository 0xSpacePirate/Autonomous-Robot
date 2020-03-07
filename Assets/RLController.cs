using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RLBalance : MonoBehaviour
{

    // Use this for initialization

    private int NumberOfStates = 12, goal = 11, maxEpochs = 1000;
    private double gamma = 0.5, learnRate = 0.5;
    private int[][] FeasibleTransitions;
    private double[][] RewardMatrix, Q;

    void Start()
    {
        Debug.Log("RL has been initiated!");
        this.FeasibleTransitions = CreateMaze(NumberOfStates);
        this.RewardMatrix = CreateReward(NumberOfStates);
        this.Q = CreateQuality(NumberOfStates);
        Train();
        Balance();
        Debug.Log("RL has ended!");
    }

    // Update is called once per frame
    void Update()
    {

    }

    private int[][] CreateMaze(int NumberOfStates)
    {
        int[][] FeasibleTransitions = new int[ns][];
        for (int i = 0; i < NumberOfStates; ++i) FT[i] = new int[ns];
        FT[0][1] = FT[0][4] = FT[1][0] = FT[1][5] = FT[2][3] = 1;
        FT[2][6] = FT[3][2] = FT[3][7] = FT[4][0] = FT[4][8] = 1;
        FT[5][1] = FT[5][6] = FT[5][9] = FT[6][2] = FT[6][5] = 1;
        FT[6][7] = FT[7][3] = FT[7][6] = FT[7][11] = FT[8][4] = 1;
        FT[8][9] = FT[9][5] = FT[9][8] = FT[9][10] = FT[10][9] = 1;
        FT[11][11] = 1;  // the final Goal
        return FeasibleTransitions;
    }

    private double[][] CreateReward(int NumberOfStates)
    {
        double[][] RewardMatrix = new double[NumberOfStates][];
        for (int i = 0; i < NumberOfStates; ++i) R[i] = new double[NumberOfStates];
        R[0][1] = R[0][4] = R[1][0] = R[1][5] = R[2][3] = -0.4;
        R[2][6] = R[3][2] = R[3][7] = R[4][0] = R[4][8] = -0.4;
        R[5][1] = R[5][6] = R[5][9] = R[6][2] = R[6][5] = -0.4;
        R[6][7] = R[7][3] = R[7][6] = R[7][11] = R[8][4] = -0.4;
        R[8][9] = R[9][5] = R[9][8] = R[9][10] = R[10][9] = -0.4;
        R[10][7] = R[11][3] = R[11][6] = R[7][11] = R[12][4] = -0.4;
        R[12][9] = R[13][5] = R[13][8] = R[9][10] = R[14][9] = -0.4;
        R[14][7] = R[15][3] = R[15][6] = R[7][11] = R[16][4] = -0.4;
        R[18][9] = R[17][5] = R[17][8] = R[9][10] = R[18][9] = -0.4;
        R[18][11] = 20.0; // and the goal provides the most reward
        return R;
    }

    private double[][] CreateQuality(int NumberOfStates)
    {
        double[][] Q = new double[NumberOfStates][];
        for (int i = 0; i < NumberOfStates; ++i)
            Q[i] = new double[NumberOfStates];
        return Q;
    }

    private List<int> GetPossibleNextStates(int s, int[][] FeasibleTransitions)
    {
        List<int> result = new List<int>();
        for (int j = 0; j < FeasibleTransitions.Length; ++j)
            if (FeasibleTransitions[s][j] == 1) result.Add(j);
        return result;
    }

    private int GetRandNextState(int s, int[][] FeasibleTransitions)
    {
        List<int> possibleNextStates = GetPossibleNextStates(s, FeasibleTransitions);
        int currentState = possibleNextStates.Count;
        return possibleNextStates[rnd.Next(0, currentState)];
    }

    private void Train()
    {
        for (int epoch = 0; epoch < this.maxEpochs; ++epoch)
        {
            int currentState = rnd.Next(0, this.Rewards.Length);
            while (true)
            {
                int nextState = GetRandNextState(currState, this.FeasibleTransitions);
                List<int> PossibleNextNextStates = GetPossibleNextStates(nextState, this.FeasibleTransitions);
                double maxQ = double.MinValue;
                for (int j = 0; j < PossibleNextNextStates.Count; ++j)
                {
                    int nextNextState = PossibleNextNextStates[j];
                    double q = Q[nextState][nextNextState];
                    if (q > maxQ) maxQ = q;
                }
                this.Q[currentState][nextState] = ((1 - this.learningRate) * this.Q[currentState][nextState])
                                                    + (learningRate * (R[currentState][nextState] + (gamma * maxQ)));
                currentState = nextState;
                if (currentState == this.goal) break;
            }
        }
    }

    private void Balance()
    {
        int current = 0; int next; // current is 0?
        while (curr != goal)
        {
            next = ArgMax(this.Q[current]);
            Debug.Log(next + "->");
            current = next;
        }
    }

    private int ArgMax(double[] vector)
    {
        double maxVal = vector[0]; int idx = 0;
        for (int i = 0; i < vector.Length; ++i)
        {
            if (vector[i] > maxVal)
            {
                maxVal = vector[i]; idx = i;
            }
        }
        return idx;
    }

    private void Print(double[][] Q)
    {
        int ns = Q.Length;
        Console.WriteLine("[0] [1] . . [11]");
        for (int i = 0; i < ns; ++i)
        {
            for (int j = 0; j < ns; ++j)
            {
                Console.Write(Q[i][j].ToString("F2") + " ");
            }
            Console.WriteLine();
        }
    }
}
