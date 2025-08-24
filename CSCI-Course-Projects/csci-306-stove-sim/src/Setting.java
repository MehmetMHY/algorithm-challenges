/**
 * Setting Class
 * 
 * @author Cody Ullestad
 * @author Mehmet Yilmaz
 * 
 */

public enum Setting {
	OFF("---"),LOW("--+"),MEDIUM("-++"),HIGH("+++"); // Declaration of Enum variables

	private String temp; // Current temperature (---, --+, -++, or +++)

	Setting (String setting){
		temp=setting;
	}

	public String toString() {
		return temp;
	}
}