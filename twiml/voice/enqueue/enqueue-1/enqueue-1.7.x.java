import com.twilio.twiml.voice.Enqueue;
import com.twilio.twiml.VoiceResponse;
import com.twilio.twiml.TwiMLException;


public class Example {
    public static void main(String[] args) {
        Enqueue enqueue = new Enqueue.Builder("support")
            .waitUrl("wait-music.xml").build();
        VoiceResponse response = new VoiceResponse.Builder().enqueue(enqueue)
            .build();

        try {
            System.out.println(response.toXml());
        } catch (TwiMLException e) {
            e.printStackTrace();
        }
    }
}
