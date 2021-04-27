public delegate void MovementDelegate(float inputX, float inputY, bool isWalking, bool isRunning, bool isIdle, bool isCarrying,
    ToolEffect toolEffect, bool isUsingToolRight, bool isUsingToolLeft, bool isUsingToolUp, bool isUsingToolDown,
    bool isLiftingToolRight, bool isLiftingToolLeft, bool isLiftingToolUp, bool isLifitingToolDown,
    bool isPickingRight, bool isPickingLeft, bool isPickingUp, bool isPickingDown,
    bool isSwingingToolRight, bool isSwingingToolLeft, bool isSwingingToolUp, bool isSwingingToolDown,
    bool idleUp, bool idleDown, bool idleLeft, bool idleRight);

public static class EventHandler
{

    public static event MovementDelegate MovementEvent;
    public static void CallMovementEvent(float inputX, float inputY, bool isWalking, bool isRunning, bool isIdle, bool isCarrying,
    ToolEffect toolEffect, bool isUsingToolRight, bool isUsingToolLeft, bool isUsingToolUp, bool isUsingToolDown,
    bool isLiftingToolRight, bool isLiftingToolLeft, bool isLiftingToolUp, bool isLifitingToolDown,
    bool isPickingRight, bool isPickingLeft, bool isPickingUp, bool isPickingDown,
    bool isSwingingToolRight, bool isSwingingToolLeft, bool isSwingingToolUp, bool isSwingingToolDown,
    bool idleUp, bool idleDown, bool idleLeft, bool idleRight)
    {
        if (MovementEvent!=null)
        {
            MovementEvent( inputX,  inputY,  isWalking,  isRunning,  isIdle,  isCarrying,
                 toolEffect,  isUsingToolRight,  isUsingToolLeft,  isUsingToolUp,  isUsingToolDown,
                 isLiftingToolRight,  isLiftingToolLeft,  isLiftingToolUp,  isLifitingToolDown,
                 isPickingRight,  isPickingLeft,  isPickingUp,  isPickingDown,
                 isSwingingToolRight,  isSwingingToolLeft,  isSwingingToolUp,  isSwingingToolDown,
                 idleUp,  idleDown,  idleLeft,  idleRight);
        }
    }
}