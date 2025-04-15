ublic static void saveFileList(String folderPath, String outputFile) throws IOException {
        var out = new BufferedWriter(new FileWriter(outputFile));
        Arrays.stream(new File(folderPath).listFiles())
              .filter(File::isFile)
              .map(f -> f.getName().replaceFirst("\\.[^.]+$", ""))
              .forEach(name -> {
                  try { out.write(name); out.newLine(); } catch (IOException ignored) {}
              });
        out.close();
    }

    public static boolean deleteFile(String path) {
        return new File(path).delete();
    }

    public static void main(String[] args) throws IOException {
        saveFileList("C:\\path\\to\\your\\folder", "file_list.txt");
        // deleteFile("C:\\path\\to\\your\\folder\\unwanted.txt");
    }
