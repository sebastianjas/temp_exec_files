import java.io.*;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

public class ZipTxtProcessor {
    public static void main(String[] args) {
        String zipFilePath = "your_file.zip";

        try (ZipFile zipFile = new ZipFile(zipFilePath)) {
            Enumeration<? extends ZipEntry> entries = zipFile.entries();

            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();

                if (!entry.isDirectory() && entry.getName().endsWith(".txt")) {
                    try (InputStream is = zipFile.getInputStream(entry);
                         BufferedReader reader = new BufferedReader(new InputStreamReader(is))) {

                        System.out.println("Reading: " + entry.getName());

                        String line;
                        while ((line = reader.readLine()) != null) {
                            // Process the line here
                            System.out.println(line);
                        }

                    } catch (IOException e) {
                        System.err.println("Error reading entry: " + entry.getName());
                        e.printStackTrace();
                    }
                }
            }

        } catch (IOException e) {
            System.err.println("Error opening ZIP file.");
            e.printStackTrace();
        }
    }
}
