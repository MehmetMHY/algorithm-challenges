/**
 * Burner Class
 * 
 * @author Cody Ullestad
 * @author Mehmet Yilmaz
 * 
 */

public class Burner {
	private Setting mySetting; // current temperature setting for stove
	private int timer; // timer for transitions between different temps
	public final static int TIME_DURATION=2; // constant time interval
	private int burnNotch; // index tracker for time durations when stove is "burning"
	private int settingNotch; // index tracker for time duration when stove is "cooling"
	private Temperature myTemperature; // current temperature for stove
	public static String printThis; // variable used to help determine what displayStove(), in the Burner class, should print
	
	private enum Temperature{
		BLAZING,HOT,WARM,COLD
	}

	// Constructor for Burner class:
	public Burner() {
		super();
		this.myTemperature = Temperature.COLD;
		this.mySetting = Setting.OFF;
		this.burnNotch=0;
		this.settingNotch=0;
	}
	
	public Setting getMySetting() {
		return mySetting;
	}

	public Temperature getMyTemperature() {
		return myTemperature;
	}

	// Used to increase or decrease temperature setting (labelled + and/or -):
	public void plusButton() {
		switch(this.mySetting) {
		case OFF:
			this.mySetting=Setting.LOW;
			this.timer=TIME_DURATION;
			this.settingNotch=1;
			break;
		case LOW:
			this.mySetting=Setting.MEDIUM;
			this.timer=TIME_DURATION;
			this.settingNotch=2;
			break;
		case MEDIUM:
			this.mySetting=Setting.HIGH;
			this.timer=TIME_DURATION;
			this.settingNotch=3;
			break;
		case HIGH:
			this.mySetting=Setting.HIGH;
			break;
		}
	}

	// Used to subtract the timer variable per iteration/Passing-Of-Time
	public void minusButton() {
		switch(this.mySetting) {
		case HIGH:
			this.mySetting=Setting.MEDIUM;
			this.timer=TIME_DURATION;
			this.settingNotch=2;
			break;
		case MEDIUM:
			this.mySetting=Setting.LOW;
			this.timer=TIME_DURATION;
			this.settingNotch=1;
			break;
		case LOW:
			this.mySetting=Setting.OFF;
			this.timer=TIME_DURATION;
			this.settingNotch=0;
			break;
		case OFF:
			this.mySetting=Setting.OFF;
			this.timer=TIME_DURATION;
			break;
		}

	}

	// Updates the temperature status of a burner based on the time
	public void updateTemperature() {
		if(this.timer>1) {
			--this.timer;
		}else {
			if(this.settingNotch>this.burnNotch) {
				switch(this.myTemperature) {
				case COLD:
					this.myTemperature=Temperature.WARM;
					++this.burnNotch;
					break;
				case WARM:
					this.myTemperature=Temperature.HOT;
					++this.burnNotch;
					break;
				case HOT:
					this.myTemperature=Temperature.BLAZING;
					++this.burnNotch;
					break;
				case BLAZING:
					this.myTemperature=Temperature.BLAZING;
				}

			}
			if(this.settingNotch<this.burnNotch){
				switch(this.myTemperature) {
				case COLD:
					this.myTemperature=Temperature.COLD;
				case WARM:
					this.myTemperature=Temperature.COLD;
					--this.burnNotch;
					break;
				case HOT:
					this.myTemperature=Temperature.WARM;
					--this.burnNotch;
					break;
				case BLAZING:
					this.myTemperature=Temperature.HOT;
					--this.burnNotch;
					break;
				}
			}
			if(burnNotch!=settingNotch) {
				this.timer=TIME_DURATION;
			}
		}

	}

	// Used to help print the temperature status of a burner:
	public void printTemperature() {
		switch(this.myTemperature) {
		case COLD:
			printThis = "coool";
			break;
		case WARM:
			printThis = "warm";
			break;
		case HOT:
			printThis = "CAREFUL";
			break;
		case BLAZING:
			printThis = "VERY HOT! DON'T TOUCH";
			break;
		}
	}
}


