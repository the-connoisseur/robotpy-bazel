import wpilib

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot-wide initialization code.

        This is called when the robot is first powered on. It is called
        exactly one time.
        """
        pass

    def robotPeriodic(self):
        """Periodic code for all modes.

        This is called each time a new packet is received from the
        driver station.
        """
        pass

    # TODO(Sanjay): Why are these hidden?
    # def simulationInit(self):
    #     """Robot-wide simulation initialization code.
    #
    #     This is called when the robot is first started. It is called
    #     exactly one time after robotInit is called, only when the robot
    #     is in simulation.
    #     """
    #     pass
    #
    # def simulationPeriodic(self):
    #     """Periodic simulation code.
    #
    #     This is called in a simulated robot after user code executes.
    #     """
    #     pass

    def driverStationConnected(self):
        """Code that needs to know the DS state.

        This is called when the DS is connected. Code that needs to know
        things like alliance information should go here.
        """
        pass

    def autonomousInit(self):
        """Initialization code for autonomous mode.

        This is called each time the robot enters autonomous mode.
        """
        pass

    def autonomousPeriodic(self):
        """Periodic code for autonomous mode.

        This is called each time a new packet is received from the
        driver station and the robot is in autonomous mode.
        """
        pass

    def autonomousExit(self):
        """Exit code for autonomous mode.

        This is called each time the robot exits autonomous mode.
        """
        pass

    def disabledInit(self):
        """Initialization code for disabled mode.

        This is called each time the robot enters disabled mode.
        """
        pass

    def disabledPeriodic(self):
        """Periodic code for disabled mode.

        This is called each time a new packet is received from the
        driver station and the robot is in disabled mode.
        """
        pass

    def disabledExit(self):
        """Exit code for disabled mode.

        This is called each time the robot exits disabled mode.
        """
        pass

    def teleopInit(self):
        """Initialization code for teleop mode.

        This is called each time the robot enters teleop mode.
        """
        pass

    def teleopPeriodic(self):
        """Periodic code for teleop mode.

        This is called each time a new packet is received from the
        driver station and the robot is in teleop mode.
        """
        pass

    def teleopExit(self):
        """Exit code for teleop mode.

        This is called each time the robot exits teleop mode.
        """
        pass

    def testInit(self):
        """Initialization code for test mode.

        This is called each time the robot enters test mode.
        """
        pass

    def testPeriodic(self):
        """Periodic code for test mode.

        This is called each time a new packet is received from the
        driver station and the robot is in test mode.
        """
        pass

    def testExit(self):
        """Exit code for test mode.

        This is called each time the robot exits test mode.
        """
        pass


if __name__ == '__main__':
    wpilib.run(MyRobot)
