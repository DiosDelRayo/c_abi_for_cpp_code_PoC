#include <cstdint>
#include <cstring>
#include <string>
#include <QString>
#include <QByteArray>
#include <QCryptographicHash>

extern "C" {
  void hash(const char* bytes, char** output) {
    QString input(bytes);
    QByteArray inputBytes = input.toUtf8();
    QByteArray hashBytes = QCryptographicHash::hash(inputBytes, QCryptographicHash::Sha256);
    QString outputString = hashBytes.toHex();
    QByteArray outputBytes = outputString.toUtf8();
    *output = new char[outputBytes.size() + 1];
    std::strcpy(*output, outputBytes.constData());
  }
}
